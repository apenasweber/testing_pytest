import pytest

def test_our_first_test() -> None:
    assert 1 == 1

@pytest.mark.skip
def test_should_be_skipped() -> None:
    assert 1 == 2

@pytest.mark.skipif(4>1, reason="4 more than 1, so i skipped")
def test_should_be_skipped_if() -> None:
    assert 1 == 2

@pytest.mark.xfail
def test_dont_care_if_fails() -> None:
    assert 1 == 2


class Company:
    def __init__(self, name:str, stock:str):
        self.name = name
        self.stock = stock

    def __str__(self):
        return f"{self.name}:{self.stock}"

@pytest.fixture
def company() -> Company:
    return Company(name="Fiver", stock="FVRR")

def test_with_fixture(company: Company) -> None:
    print(f"printinh {company} from fixture")


@pytest.mark.parametrize(
    "company_name",
    ["Tik Tok","Instagram","Twitch"],
    ids=["tiktok test", "insta test", "twitch test"]
)

def test_parametrized(company_name:str) -> None:
    print(f"\nTest With {company_name}")

def raise_covid19_exception() -> None:
    raise ValueError("Corona Exception")

def test_raise_covid19_exception_should_pass() -> None:
    with pytest.raises(ValueError) as e:
        raise_covid19_exception()
    assert "Corona Exception" == str(e.value)