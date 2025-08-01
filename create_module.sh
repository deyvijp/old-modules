# filepath: create_odoo_module.sh

read -p "Nombre del módulo: " MODULE
read -p "¿Es un módulo Owl? (s/n): " IS_OWL

mkdir -p "$MODULE"/{models,views,security}

touch "$MODULE"/__init__.py
touch "$MODULE"/__manifest__.py
touch "$MODULE"/models/__init__.py
touch "$MODULE"/models/${MODULE}_model.py
touch "$MODULE"/views/${MODULE}_views.xml
touch "$MODULE"/security/ir.model.access.csv

if [[ "$IS_OWL" =~ ^[sS]$ ]]; then
    mkdir -p "$MODULE"/static/src/{components,models,styles,utils}
    touch "$MODULE"/static/src/components/.gitkeep
    touch "$MODULE"/static/src/models/.gitkeep
    touch "$MODULE"/static/src/styles/.gitkeep
    touch "$MODULE"/static/src/utils/.gitkeep
fi

echo "¡Módulo '$MODULE' creado con éxito!"
