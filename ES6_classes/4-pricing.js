/* eslint-disable */
import Currency from './3-currency';
/* eslist-enable */

export default class Pricing {
  constructor(amount, currency) {
    this.amount = amount;
    this.currency = currency;
  }

  get amount() { return this._amount; }

  get currency() { return this._currency; }

  set amount(amount) { this._amount = amount; }

  set currency(currency) { this._currency = currency; }

  displayFullPrice() { return `${this._amount} ${this.currency._name} (${this.currency._code})`; }

  static convertPrice(amount, conversionRate) { return amount * conversionRate; }
}
