#!/bin/bash

# Script para crear la rama "pilataxi" desde la rama de Claude
# Ejecutar este script desde tu máquina local (NO desde Claude Code)

set -e  # Salir si hay algún error

echo "================================================"
echo "  Creando rama 'pilataxi' para el examen"
echo "================================================"
echo ""

# Colores para output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Verificar que estamos en un repositorio git
if [ ! -d ".git" ]; then
    echo -e "${RED}❌ Error: No estás en un repositorio git${NC}"
    echo "Por favor ejecuta este script desde la raíz del repositorio"
    exit 1
fi

echo -e "${YELLOW}📡 Paso 1: Fetch de cambios remotos...${NC}"
git fetch origin

echo ""
echo -e "${YELLOW}🔍 Paso 2: Verificando que existe la rama de Claude...${NC}"
if git show-ref --verify --quiet refs/remotes/origin/claude/implement-cicd-pipeline-01CARCXuC85kDCxj8TbJXh1X; then
    echo -e "${GREEN}✅ Rama encontrada${NC}"
else
    echo -e "${RED}❌ Error: No se encontró la rama de Claude en el remoto${NC}"
    exit 1
fi

echo ""
echo -e "${YELLOW}🌿 Paso 3: Creando rama 'pilataxi'...${NC}"
if git show-ref --verify --quiet refs/heads/pilataxi; then
    echo -e "${YELLOW}⚠️  La rama 'pilataxi' ya existe localmente${NC}"
    echo "¿Quieres eliminarla y recrearla? (s/n)"
    read -r respuesta
    if [ "$respuesta" = "s" ] || [ "$respuesta" = "S" ]; then
        git branch -D pilataxi
        echo -e "${GREEN}✅ Rama local eliminada${NC}"
    else
        echo -e "${RED}❌ Operación cancelada${NC}"
        exit 1
    fi
fi

git checkout -b pilataxi origin/claude/implement-cicd-pipeline-01CARCXuC85kDCxj8TbJXh1X
echo -e "${GREEN}✅ Rama 'pilataxi' creada${NC}"

echo ""
echo -e "${YELLOW}📤 Paso 4: Pushing rama 'pilataxi' al remoto...${NC}"
git push -u origin pilataxi
echo -e "${GREEN}✅ Rama pusheada exitosamente${NC}"

echo ""
echo -e "${YELLOW}🗑️  Paso 5: ¿Quieres eliminar la rama antigua de Claude del remoto? (s/n)${NC}"
read -r respuesta
if [ "$respuesta" = "s" ] || [ "$respuesta" = "S" ]; then
    git push origin --delete claude/implement-cicd-pipeline-01CARCXuC85kDCxj8TbJXh1X
    echo -e "${GREEN}✅ Rama antigua eliminada del remoto${NC}"
else
    echo -e "${YELLOW}⚠️  Rama antigua mantenida en el remoto${NC}"
fi

echo ""
echo "================================================"
echo -e "${GREEN}✅ ¡Proceso completado exitosamente!${NC}"
echo "================================================"
echo ""
echo "📊 Estado actual:"
git branch -a | grep -E "(pilataxi|claude/implement)"
echo ""
echo "🎯 Próximos pasos:"
echo "1. Verifica en GitHub que la rama 'pilataxi' existe"
echo "2. Configura los GitHub Secrets (VPS_HOST, VPS_USERNAME, VPS_SSH_KEY)"
echo "3. El pipeline CI/CD se ejecutará automáticamente"
echo ""
echo "🌐 URLs útiles:"
echo "- Repositorio: https://github.com/Padme2003/examen-practico-1"
echo "- Branches: https://github.com/Padme2003/examen-practico-1/branches"
echo "- Actions: https://github.com/Padme2003/examen-practico-1/actions"
echo ""
