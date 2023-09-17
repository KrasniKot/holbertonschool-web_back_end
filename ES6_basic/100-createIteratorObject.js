export default function createIteratorObject(report) {
  let empList = [];

  for (let dep in report["allEmployees"]) {
    for (let emp of report["allEmployees"][dep]) { empList.push(emp); }
  }
  return empList;
}
