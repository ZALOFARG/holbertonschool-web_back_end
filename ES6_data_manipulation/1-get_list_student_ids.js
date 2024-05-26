export default function getListStudentIds(listStudents) {
  const arrayId = [];
  if (listStudents instanceof Array) {
    listStudents.map((student) => arrayId.push(student.id));
  }

  return arrayId;
}
