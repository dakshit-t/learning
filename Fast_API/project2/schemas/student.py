def studentEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": str(item["name"]),
        "email": item["email"],
        "std": item["class"],
        "course": item["course_of_study"],
        "year": item["year"],
        "gpa": item["gpa"]
    }


def studentsEntity(items) -> list:
    print(items)
    return [studentEntity(item) for item in items]
