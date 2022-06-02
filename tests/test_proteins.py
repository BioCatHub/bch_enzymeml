import json

from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.build_proteins import ProteinBuilder
from bchenzymml.models.biocathub_test_model_ec_missing import model_ec_missing


def test_missing_ec():

    protein = ProteinBuilder(model_ec_missing)
    new_protein = protein.build_proteins()

