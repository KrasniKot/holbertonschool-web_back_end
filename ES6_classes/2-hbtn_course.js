export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() { return this._name; }
  get length() { return this._length; }
  get students() { return this._students; }

  set name(same) {
    if (typeof same !== 'string') {
          throw new TypeError('Name must be a string')
        }
    else { this._name = same; }
  }

  set length(lgth) {
    if (typeof lgth !== 'number') {
          throw new TypeError('Length must be a number')
        }
    else { this._length = lgth; }
  }

  set students(snts) {
    if (typeof snts !== 'object') {
          throw new TypeError('Students must be an array')
        }
    else { this._students = snts; }
  }

}
