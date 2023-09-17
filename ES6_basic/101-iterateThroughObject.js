export default function iterateThroughObject(reportWithIterator) {
  let empray = '';

  for (const emp of reportWithIterator) {
    empray += emp;
    empray += ' | ';
  }

  if (empray.length > 0) {
    empray = empray.slice(0, -3);
  }

  return empray;
}
