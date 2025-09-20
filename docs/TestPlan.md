# Test Plan – Flash Hotel

[← Back to Readme](../Readme.md)

## Manual Test Cases

| # | Action                                   | Expected Result                            | Status | Evidence |
|---|------------------------------------------|--------------------------------------------|--------|----------|
| 1 | Register new user                        | Account created, success flash message     | Passed | [Open](img/Test01.png) |
| 2 | Register with existing email             | Error “Email is already present” displayed | Passed | [Open](img/Test02.png) |
| 3 | Login with correct credentials           | Redirect to homepage, “logged in” flash    | Passed | [Open](img/Test03.png) |
| 4 | Login with wrong password                | Error flash message shown, no login/pw     | Passed | [Open](img/Test04.png) |
| 5 | Create booking (1–3 Oct)                 | Booking saved and listed under user        | Passed | [Open](img/Test05.png) |
| 6 | Attempt overlapping booking              | Validation error, prevented from saving    | Passed | [Open](img/Test06.png) |
| 7 | Edit existing booking                    | Dates updated successfully                 | Passed | [Open](img/Test07.png) |
| 8 | Delete booking                           | Booking removed from list                  | Passed | [Open](img/Test08.png) |
| 9 | Access route without login               | Redirected to login page                   | Passed | [Open](img/Test09.png) |

---

## Notes
- All tests were performed on the live deployment at [Flash Hotel on PythonAnywhere](https://dailafing.pythonanywhere.com/).
- Screenshots are saved in the `docs/img/` folder.
