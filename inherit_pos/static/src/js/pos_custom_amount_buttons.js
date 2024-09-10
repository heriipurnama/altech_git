odoo.define('inherit_pos.CustomAmountButtons', function(require) {
    "use strict";

    var PaymentScreen = require('point_of_sale.PaymentScreen');

    PaymentScreen.include({
        renderElement: function() {
            this._super();
            // Modify the amount buttons
            this.$('.input-button.button-10').text("+10,000");
            this.$('.input-button.button-20').text("+50,000");
            this.$('.input-button.button-50').text("+100,000");
        }
    });
});
