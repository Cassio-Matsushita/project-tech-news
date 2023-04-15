from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
import pytest
from tests.mocks import group_news_for_available_time as mock


@pytest.fixture
def find_news_mock_fixture(mocker):
    mocker.patch(
        "tech_news.analyzer.reading_plan.find_news",
        return_value=mock.find_news_mock,
    )


def test_reading_plan_group_news(find_news_mock_fixture):
    assert (
        ReadingPlanService().group_news_for_available_time(10)
        == mock.news_for_available_time_mock
    )

    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        ReadingPlanService().group_news_for_available_time(-1)
