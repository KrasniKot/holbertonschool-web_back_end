import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this.amount = amount;
    this.currency = currency;
  }

  get amount() { return this._amount; }

  get currency() { return this._currency; }

  set amount(amount) { this._amount = amount; }

  set currency(currency) {
    if (typeof currency === Currency) {
      this._currency = currency;
    }
    else { throw TypeError('currency must be a Currency') }
  }

  displayFullPrice() { return `${this._amount} ${this.currency._name} (${this.currency._code})`; }
}
