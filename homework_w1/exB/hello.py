print("Dang Duc Khanh")
print("DHKHMTEN_01 K20")
print("The reason learning Python is important is because it is a versatile and widely-used programming language that can be applied to various fields such as" \
      " web development, data analysis, artificial intelligence, and more. Python's simplicity and readability make it an excellent choice for beginners," \
      " while its extensive libraries and frameworks provide powerful tools for experienced developers." \
      " By learning Python, individuals can enhance their problem-solving skills, improve their career prospects, and contribute to innovative projects across different industries.")
print("I'm from Thanh Hoa.")


repo_url = "https://github.com/Hikari-de/Python_Private"
first_commit = "2bdfbc7"
second_commit = "c92a65c"


if any(x is None for x in [repo_url, first_commit, second_commit]):
    print("Chua hoan thanh: dien URL va hai ma commit sau khi thao tac that.")
else:
    assert str(repo_url).startswith("https://github.com/")
    assert len(str(first_commit)) >= 7 and len(str(second_commit)) >= 7
    assert first_commit != second_commit
    print("Da dien minh chung; leader se kiem tra repo va lich su.")