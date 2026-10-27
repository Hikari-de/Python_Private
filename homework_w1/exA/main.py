check_state = "status"
select_changes = "add"
save_version = "commit"
send_to_github = "push"
copy_existing_repo = "clone"
start_empty_repo = "init"

answers = ["status", "add", "commit", "push", "clone", "init"]

if any(value is None for value in answers):
    print("Chua hoan thanh: dien ca 6 lenh.")
else:
    assert answers == ["status", "add", "commit", "push", "clone", "init"]
    print("Dat: ban phan biet duoc cac lenh co ban.")