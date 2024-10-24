import pytest
import main
import user_inputs


def test_id_is_ok():
    assert user_inputs.running_app()
