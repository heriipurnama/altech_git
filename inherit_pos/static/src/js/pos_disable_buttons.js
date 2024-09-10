odoo.define('inherit_pos.DisableButtons', function(require) {
    "use strict";

    var screens = require('point_of_sale.screens');

    screens.ActionpadWidget.include({
        renderElement: function() {
            this._super();
            // Disable Price Button
            this.$('.set-price').off('click');
            // Disable Discount Button
            this.$('.set-discount').off('click');
        }
    });
});
