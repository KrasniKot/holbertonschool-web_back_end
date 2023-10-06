export default function updateStudentGradeByCity(stdnts, city, newGrades) {
  return stdnts
    .filter((student) => student.location == city)
    .map((student) => {
      const nge = newGrades.filter((ng) => ng.studentId === student.id)
        .map((ng) => ng.grade)[0]
      student.grade = nge || 'N/A';
      return student;
    });
}
