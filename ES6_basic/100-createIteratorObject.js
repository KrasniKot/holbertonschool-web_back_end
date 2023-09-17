export default function createIteratorObject(report) {
  const empList = [];

  /* eslint-disable */
  for (const dep in report.allEmployees) {
    for (const emp of report.allEmployees[[dep]) { empList.push(emp); }
  }

  return empList;
}
