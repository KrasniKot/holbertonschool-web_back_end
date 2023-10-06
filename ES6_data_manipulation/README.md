# ES6 data manipulation

## Tasks:

### Task 0 Basic list of objects:
Create a function named `getListStudents` that returns an array of objects.
Each object should have three attributes: `id` (Number), `firstName` (String), and `location` (String).
The array contains the following students in order:
* Guillaume, id: 1, in San Francisco
* James, id: 2, in Columbia
* Serena, id: 5, in San Francisco

### Task 1 More mapping:
Create a function `getListStudentIds` that returns an array of ids from a list of object.
This function is taking one argument which is an array of objects - and this array is the same format as `getListStudents` from the previous task.
If the argument is not an array, the function is returning an empty array.
You must use the `map` function on the array.

### Task 2 Filter:
Create a function `getStudentsByLocation` that returns an array of objects who are located in a specific city.
It should accept a list of students (from `getListStudents`) and a `city` (string) as parameters.
You must use the `filter` function on the array.

### Task 3 Reudce:
Create a function `getStudentIdsSum` that returns the sum of all the student ids.
It should accept a list of students (from `getListStudents`) as a parameter.
You must use the `reduce` function on the array.

### Task 4 Combine:
Create a function `updateStudentGradeByCity` that returns an array of students for a specific city with their new grade
It should accept a list of students (from `getListStudents`), a `city` (String), and `newGrades` (Array of “grade” objects) as parameters.
`newGrades` is an array of objects with this format:

`{ studentId: 31, grade: 78, }`
If a student doesn’t have grade in newGrades, the final grade should be `N/A`.
You must use `filter` and `map` combined.

### Task 5 Typed Arrays:
### Task 6 Set data structure:
### Task 7 More set data structure:
### Task 8 Clean set:
### Task 9 Map data structure:
### Task 10 More map data structure: