export default function getStudentsByLocation(getListStudents, city) {
  const result = getListStudents.filter((student) => student.location === city);
  return result;
}
