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

function renderRecipes() {
    const grid = document.getElementById('recipe-grid');
    grid.innerHTML = filteredRecipes.map(recipe => `
        <div class="recipe-card" onclick="openDetails(${recipe.id})">
            <img src="https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=500&q=80" alt="${recipe.name}" class="recipe-image">
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
                <a href="${recipe.grocery_notes_url}" class="btn-grocery" onclick="event.stopPropagation();">
                    📝 Open Grocery List
                </a>
            </div>
        </div>
    `).join('');

    document.getElementById('item-count').innerText = `${filteredRecipes.length} Recipes`;
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

        <a href="${recipe.grocery_notes_url}" class="btn-grocery">
            📝 Create Grocery List in Notes
        </a>
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
