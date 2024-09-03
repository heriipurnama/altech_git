from odoo.tests import TransactionCase

class TestMaterial(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestMaterial, self).setUp(*args, **kwargs)
        self.Supplier = self.env['material.supplier']
        self.Material = self.env['material.material']

        # Create a test supplier
        self.supplier = self.Supplier.create({'name': 'Test Supplier'})

    def test_create_material(self):
        # Create material
        material = self.Material.create({
            'code': 'M001',
            'name': 'Test Material',
            'material_type': 'fabric',
            'buy_price': 120,
            'supplier_id': self.supplier.id
        })
        self.assertEqual(material.name, 'Test Material')
        self.assertEqual(material.material_type, 'fabric')
        self.assertEqual(material.buy_price, 120)

    def test_buy_price_validation(self):
        # Try to create material with buy price less than 100
        with self.assertRaises(ValidationError):
            self.Material.create({
                'code': 'M002',
                'name': 'Invalid Material',
                'material_type': 'jeans',
                'buy_price': 50,
                'supplier_id': self.supplier.id
            })

    def test_update_material(self):
        # Create material
        material = self.Material.create({
            'code': 'M001',
            'name': 'Test Material',
            'material_type': 'fabric',
            'buy_price': 120,
            'supplier_id': self.supplier.id
        })

        # Update material
        material.write({'name': 'Updated Material', 'buy_price': 130})
        self.assertEqual(material.name, 'Updated Material')
        self.assertEqual(material.buy_price, 130)

    def test_delete_material(self):
        # Create material
        material = self.Material.create({
            'code': 'M003',
            'name': 'Material to delete',
            'material_type': 'cotton',
            'buy_price': 150,
            'supplier_id': self.supplier.id
        })

        # Delete material
        material_id = material.id
        material.unlink()
        material_deleted = self.Material.search([('id', '=', material_id)])
        self.assertFalse(material_deleted)
