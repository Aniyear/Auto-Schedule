import os
import sys
import random

# Allow imports from the repository root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts.chromosome import Chromosome
from scripts.gene import Gene

def test_physical_education_mutation_does_not_change_room():
    gene = Gene(
        group="IT-2201",
        course="Physical Education",
        type="Practice",
        day="Mon",
        time="08:00",
        room="Gym",
    )
    chromosome = Chromosome([gene])
    # Seed randomness so the mutation is deterministic
    random.seed(5)
    chromosome.mutate(
        timeslots=["09:00", "10:00"],
        days=["Tue", "Wed"],
        rooms=["C1.2.127"],
    )
    # Room should never change for physical education
    assert gene.room == "Gym"
    # Either day or time should be mutated away from the original values
    assert gene.day != "Mon" or gene.time != "08:00"
