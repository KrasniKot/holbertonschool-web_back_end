export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  [Symbol.toPrimitive](obj) {
    if (obj === 'number') return this._size;
    return this._location;
  }
}
