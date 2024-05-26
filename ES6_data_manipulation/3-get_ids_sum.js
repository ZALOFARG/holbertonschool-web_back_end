export default function getStudentsIdsSum(getListStudents) {
  const result = getListStudents.reduce((curr, acc) => curr + acc.id, 0);
  return result;
}
