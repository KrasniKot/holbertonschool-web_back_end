export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  set name(same) {
    if (typeof same !== 'string') {
      throw new TypeError('Name must be a string');
    } else {
      this._name = same;
    }
  }

  set length(lgth) {
    if (typeof lgth !== 'number') {
      throw new TypeError('Length must be a number');
    } else {
      this._length = lgth;
    }
  }

  set students(snts) {
    if (!Array.isArray(snts)) {
      throw new TypeError('Students must be an array');
    } else {
      this._students = snts;
    }
  }

  get name() { return this._name; }
  get length() { return this._length; }
  get students() { return this._students; }
}
