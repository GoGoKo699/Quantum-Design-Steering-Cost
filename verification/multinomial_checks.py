#!/usr/bin/env python3
"""Independent finite checks of charge-conserving multinomial steering."""
from fractions import Fraction as F
from math import factorial
from itertools import product
from collections import defaultdict
import json
import numpy as np


def counts(k, d):
    if d == 1:
        yield (k,)
    else:
        for a in range(k + 1):
            for tail in counts(k - a, d - 1):
                yield (a,) + tail


def multinomial(n):
    k, d = sum(n), len(n)
    c = factorial(k)
    for x in n:
        c //= factorial(x)
    return F(c, d ** k)


def reference_distribution(q, k_minus_one):
    r = defaultdict(F)
    for n in counts(k_minus_one, len(q)):
        r[-sum(x*y for x,y in zip(n,q))] += multinomial(n)
    return dict(r)


def exact_check(q, k):
    d = len(q)
    mean = F(sum(q), d)
    variance = sum((F(x)-mean)**2 for x in q)/d
    r = reference_distribution(q, k-1)
    rmean = sum(F(x)*p for x,p in r.items())
    rvar = sum((F(x)-rmean)**2*p for x,p in r.items())
    first = [F(0) for _ in q]
    second = [[F(0) for _ in q] for _ in q]
    sectors = defaultdict(lambda: [F(0) for _ in q])
    charge_mean_variance = F(0)
    for n in counts(k,d):
        p = multinomial(n)
        t = -sum(x*y for x,y in zip(n,q))
        probs = [F(x,k) for x in n]
        charge_mean_variance += p*(sum(F(x)*a for x,a in zip(q,probs))-mean)**2
        for i in range(d):
            first[i] += p*probs[i]
            sectors[t][i] += p*probs[i]
            for j in range(d):
                second[i][j] += p*probs[i]*probs[j]
    assert first == [F(1,d)]*d
    assert rvar == (k-1)*variance
    assert charge_mean_variance == variance/k
    for t,a in sectors.items():
        assert a == [r.get(t+q[i],F(0))/d for i in range(d)]
    for i in range(d):
        for j in range(d):
            target = F(1,d*d) + F(d-1,k*d*d) if i==j else F(k-1,k*d*d)
            assert second[i][j] == target
            if k==d+1:
                assert second[i][j] == F(2 if i==j else 1,d*(d+1))
    lam_diag=F(k+d-1,k*d*d)
    lam_off=F(2*(k-1),k*d*d)
    haar=F(2,d*(d+1))
    delta=(d*abs(lam_diag-haar)+F(d*(d-1),2)*abs(lam_off-haar))/2
    expected_delta=F((d-1)*abs(d+1-k),k*d*(d+1))
    assert delta == expected_delta
    return dict(q=q,K=k,D=d,V_A=str(variance),V_R=str(rvar),
                output_charge_variance=str(charge_mean_variance),
                half_trace_moment_error=str(delta),
                exact_design=(delta==0),charge_support=len(r))


def povm_check(q,k):
    d=len(q)
    r=reference_distribution(q,k-1)
    inputs=defaultdict(list)
    for i in range(d):
        for n in r:
            inputs[n-q[i]].append((i,n))
    grams={t:np.zeros((len(b),len(b)),complex) for t,b in inputs.items()}
    moment=np.zeros((d*d,d*d),complex)
    total_prob=0.0
    max_steering_error=0.0
    for n in counts(k,d):
        t=-sum(a*b for a,b in zip(n,q))
        p_n=float(multinomial(n))
        basis=inputs[t]
        # Fix the redundant global phase; ternary relative phases kill all
        # non-pairing degree-(2,2) monomials.
        for phase_tail in product(range(3),repeat=d-1):
            phase=(0,)+phase_tail
            phase_factors=np.exp(2j*np.pi*np.array(phase)/3)
            psi=np.sqrt(np.array(n)/k)*phase_factors
            p=p_n/(3**(d-1))
            measurement_bra=np.array([
                np.sqrt(d*p*n[i]/k/float(r[nr]))*phase_factors[i]
                for i,nr in basis])
            grams[t]+=np.outer(measurement_bra.conj(),measurement_bra)
            steered=np.zeros(d,complex)
            for a,(i,nr) in enumerate(basis):
                steered[i]+=np.sqrt(float(r[nr])/d)*measurement_bra[a]
            max_steering_error=max(max_steering_error,
                                   float(np.max(abs(steered-np.sqrt(p)*psi))))
            ket2=np.kron(psi,psi)
            moment+=p*np.outer(ket2,ket2.conj())
            total_prob+=p
    max_povm_defect=max(float(np.max(abs(g-np.eye(g.shape[0])))) for g in grams.values())
    swap=np.zeros_like(moment)
    diag=np.zeros_like(moment)
    for i in range(d):
        diag[i*d+i,i*d+i]=1
        for j in range(d):
            swap[i*d+j,j*d+i]=1
    formula=(k-1)/(k*d*d)*(np.eye(d*d)+swap)+(d+1-k)/(k*d*d)*diag
    max_moment_defect=float(np.max(abs(moment-formula)))
    assert max_povm_defect < 1e-12
    assert max_steering_error < 1e-12
    assert max_moment_defect < 1e-12
    assert abs(total_prob-1)<1e-12
    return dict(q=q,K=k,povm_defect=max_povm_defect,
                steering_defect=max_steering_error,moment_defect=max_moment_defect,
                normalization=total_prob)


if __name__=="__main__":
    examples=[]
    for q in ([0,1],[0,1,2],[0,2,5],[0,0,1,1],[0,1,1,2]):
        for k in sorted(set([1,2,3,len(q)+1,len(q)+2])):
            examples.append(exact_check(list(q),k))
    matrices=[povm_check(q,k) for q,k in [([0,1],2),([0,1],3),([0,1,2],4),([0,2,5],4)]]
    report={"status":"passed","exact_cases":len(examples),"explicit_povm_cases":len(matrices),
            "exact_results":examples,"povm_results":matrices,
            "scope":"Finite normalization, second moments, sector decomposition and POVM checks; not a proof or novelty certificate."}
    print(json.dumps(report,indent=2))

