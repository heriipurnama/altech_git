odoo.define('inherit_pos.SendReceiptByEmail', function(require) {
    "use strict";

    var models = require('point_of_sale.models');
    var rpc = require('web.rpc');

    models.Order = models.Order.extend({
        initialize: function() {
            this._super.apply(this, arguments);
        },

        finalize: function() {
            var self = this;
            this._super.apply(this, arguments);

            var client = this.get_client();
            if (client && client.email) {
                // Send receipt to the customer's email
                rpc.query({
                    model: 'pos.order',
                    method: 'send_receipt_email',
                    args: [this.export_as_JSON()],
                }).then(function() {
                    self.pos.gui.show_popup('confirm', {
                        title: 'Email Sent!',
                        body: 'The receipt has been sent to ' + client.email,
                    });
                }).catch(function() {
                    self.pos.gui.show_popup('error', {
                        title: 'Error',
                        body: 'Failed to send receipt email.',
                    });
                });
            }
        },
    });
});
