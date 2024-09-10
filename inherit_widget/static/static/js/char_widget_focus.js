odoo.define('your_module_name.CharFieldFocus', function(require) {
    "use strict";

    var fieldRegistry = require('web.field_registry');
    var FieldChar = require('web.basic_fields').FieldChar;
    var FormRenderer = require('web.FormRenderer');

    // Inherit Char Field Widget
    var CharFieldFocus = FieldChar.extend({
        // Overwrite the start method to bind focus event
        start: function() {
            var self = this;
            this._super.apply(this, arguments);

            // Bind focus event to change background color to yellow
            this.$el.on('focus', function() {
                $(this).css('background-color', 'yellow');
            });

            // Bind blur event to reset background color
            this.$el.on('blur', function() {
                $(this).css('background-color', '');
            });
        },
    });

    // Register the new field type
    fieldRegistry.add('char', CharFieldFocus);

    // Inherit FormRenderer to set focus when form is loaded
    FormRenderer.include({
        _renderView: function() {
            var self = this;
            this._super.apply(this, arguments);

            // Focus on the first char field when the form is loaded
            setTimeout(function() {
                var firstCharField = self.$('input.o_field_char').first();
                if (firstCharField.length) {
                    firstCharField.focus();
                }
            }, 100); // Small delay to ensure the field is fully rendered
        },
    });

});
