let recipes = [];
let filteredRecipes = [];

async function loadRecipes() {
    try {
        const response = await fetch('./recipes.json');
        recipes = await response.json();
        filteredRecipes = [...recipes];
        renderRecipes();
    } catch (error) {
        console.error('Error loading recipes:', error);
    }
}

function showGroceryList(id) {
    const recipe = recipes.find(r => r.id === id);
    if (!recipe) return;

    const modal = document.getElementById('grocery-modal');
    const itemsList = document.getElementById('grocery-items-list');
    const status = document.getElementById('grocery-status');

    // Display items
    itemsList.innerHTML = `
        <h4 style="margin: 0 0 10px 0; color: var(--text);">${recipe.name}</h4>
        <div style="font-family: monospace; white-space: pre-wrap;">${recipe.ingredients.join('\n')}</div>
    `;

    // Copy to clipboard
    const textToCopy = `Grocery List for ${recipe.name}:\n\n- ` + recipe.ingredients.join('\n- ');
    navigator.clipboard.writeText(textToCopy).then(() => {
        status.style.display = 'block';
        setTimeout(() => { status.style.opacity = '0'; setTimeout(() => { status.style.display = 'none'; status.style.opacity = '1'; }, 500); }, 3000);
    });

    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeGroceryModal() {
    document.getElementById('grocery-modal').classList.remove('active');
    if (!document.getElementById('recipe-modal').classList.contains('active')) {
        document.body.style.overflow = 'auto';
    }
}

function renderRecipes() {
    const grid = document.getElementById('recipe-grid');
    grid.innerHTML = filteredRecipes.map(recipe => `
        <div class="recipe-card" onclick="openDetails(${recipe.id})">
            <button class="btn-card-delete" onclick="event.stopPropagation(); deleteRecipe(${recipe.id})">DELETE</button>
            <img src="${recipe.image_url || 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=500&q=80'}" alt="${recipe.name}" class="recipe-image">
            <div class="recipe-info">
                <div class="recipe-tag-row">
                    <span class="tag cuisine-tag">${recipe.cuisine}</span>
                    <span class="tag difficulty-tag">${recipe.difficulty}</span>
                </div>
                <h2 class="recipe-title">${recipe.icon} ${recipe.name}</h2>
                <div class="recipe-meta">
                    <span>⏱ ${recipe.cook_time} mins</span>
                    <span>•</span>
                    <span>🥩 ${recipe.protein}</span>
                </div>
                <div class="btn-grocery" onclick="event.stopPropagation(); showGroceryList(${recipe.id})">
                    📝 Open Grocery List
                </div>
            </div>
        </div>
    `).join('');

    document.getElementById('item-count').innerText = `${filteredRecipes.length} Recipes`;
}

function deleteRecipe(id) {
    const recipe = recipes.find(r => r.id === id);
    if (!recipe) return;
    if (confirm(`Are you sure you want to permanently delete "${recipe.name}"?`)) {
        recipes = recipes.filter(r => r.id !== id);
        filteredRecipes = filteredRecipes.filter(r => r.id !== id);
        renderRecipes();
        const rModal = document.getElementById('recipe-modal');
        if (rModal) rModal.classList.remove('active');
        document.body.style.overflow = 'auto';
    }
}

function filterCuisine(cuisine) {
    // Update active chip UI
    const chips = document.querySelectorAll('.chip');
    chips.forEach(chip => {
        if (chip.innerText === cuisine) chip.classList.add('active');
        else chip.classList.remove('active');
    });

    if (cuisine === 'All') {
        filteredRecipes = [...recipes];
    } else {
        filteredRecipes = recipes.filter(r => r.cuisine === cuisine);
    }
    renderRecipes();
}

function openDetails(id) {
    const recipe = recipes.find(r => r.id === id);
    if (!recipe) return;
    const modal = document.getElementById('recipe-modal');
    const content = document.getElementById('modal-content');

    content.innerHTML = `
        <h2 class="modal-title">${recipe.icon} ${recipe.name}</h2>
        <div class="recipe-tag-row">
            <span class="tag cuisine-tag">${recipe.cuisine}</span>
            <span class="tag">${recipe.protein}</span>
            <span class="tag">${recipe.difficulty}</span>
        </div>
        <p style="color: var(--text-light); margin-bottom: 20px;">⏱ Ready in ${recipe.cook_time} minutes</p>
        
        <h3>Ingredients</h3>
        <ul>
            ${recipe.ingredients.map(ing => `<li>${ing}</li>`).join('')}
        </ul>

        <h3>Instructions</h3>
        <ol>
            ${recipe.instructions.map(step => `<li>${step}</li>`).join('')}
        </ol>

        <div class="btn-grocery" onclick="showGroceryList(${recipe.id})">
            📝 Create Grocery List
        </div>

        <button class="btn-delete-full" onclick="deleteRecipe(${recipe.id})">
            🗑 Delete Recipe
        </button>
    `;

    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeModal() {
    const modal = document.getElementById('recipe-modal');
    modal.classList.remove('active');
    document.body.style.overflow = 'auto';
}

// Initial Load
loadRecipes();
