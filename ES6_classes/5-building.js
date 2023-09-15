export default class Building {
  constructor(sqft) {
    this.sqft = sqft;
  }

  get sqft() { return this._sqft; }

  set sqft(sqft) { this._sqft = sqft; }

  static evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
