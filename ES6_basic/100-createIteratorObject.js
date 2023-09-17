export default function createIteratorObject(report) {
  empList = [];

  for (dep in report["allEmployees"]) {
    for (emp of report["allEmployees"][dep]) { empList.push(emp); }
  }
  return empList;
}
