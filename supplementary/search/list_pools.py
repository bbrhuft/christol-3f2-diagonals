"""Write the explicit factor pools of families B2 and B3 (as actually enumerated) to
pools_B2_B3.json.  A polynomial 1 + a u + b v + c uv + d u^2 + e v^2 is stored as [a, b, c, d, e].
Usage (from this folder): python3 list_pools.py
"""
import json
import family_ab as F

P2, P3, A3 = F.b2_pool(), F.b3_pool(), set(F.b3_advertised())
json.dump({
    "format": "[a, b, c, d, e] for 1 + a u + b v + c uv + d u^2 + e v^2",
    "note": ("Pools of the November 2026 run. Each polynomial of the originally described sets was "
             "replaced separately by the lexicographic minimum of itself and its image under u <-> v. "
             "B2 enumerates products of two distinct pool elements, B3 of three. This is a restriction "
             "of the described families, not a symmetry reduction; see test_symmetry.py."),
    "B2_pool": P2,
    "B3_pool": P3,
    "B3_pool_members_not_in_described_set": [q for q in P3 if q not in A3],
}, open("pools_B2_B3.json", "w"), indent=0)
print("B2 pool", len(P2), "B3 pool", len(P3))
