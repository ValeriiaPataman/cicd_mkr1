import pytest
from src.main import count_words_and_sentences, write_result_to_file


@pytest.fixture
def sample_file():
    content = "This is a test sentence... Another test sentence! And one more?"
    file_path = "test_file.txt"
    with open(file_path, "w") as file:
        file.write(content)
    return file_path


def test_count_words_and_sentences(sample_file):
    words, sentences = count_words_and_sentences(sample_file)
    assert words == 11
    assert sentences == 3


@pytest.mark.parametrize("words, sentences, expected_output", [
    (10, 5, "Word count: 10\nSentence count: 5\n"),
    (0, 0, "Word count: 0\nSentence count: 0\n"),
    (5, 1, "Word count: 5\nSentence count: 1\n")
])
def test_write_result_to_file(tmpdir, words, sentences, expected_output):
    output_file = tmpdir.join("result.txt")
    write_result_to_file(words, sentences, output_file)
    with open(output_file) as file:
        assert file.read() == expected_output
