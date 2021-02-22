const cupcakeList = document.getElementById('cupcake-list');
const form = document.getElementById('cupcake-form');

async function getCupcakes() {
    try {
        const url = '/api/cupcakes';
        const res = await axios.get(url);
        return res.data.cupcakes;
    }
    catch(e) {
        console.log(e)
    }
}

async function addNewCupcake(data) {
    try{
        const url = '/api/cupcakes';
        const res = await axios.post(url, data);
        return res.data.cupcake;
    }
    catch {
        console.log(e)
    }
}

function createCupcakeElement(cupcake) {
    const newCupcake = document.createElement('DIV');
    newCupcake.classList.add('col-md-4')
    const image = document.createElement('IMG');
    image.src = cupcake.image;
    image.classList.add('cupcake-img');
    const title = document.createElement('H3');
    title.classList.add('display-4')
    title.innerText = cupcake.flavor;
    const details = document.createElement('P');
    details.innerText = `Size: ${cupcake.size}, Rating: ${cupcake.rating}`;
    newCupcake.append(title);
    newCupcake.append(image);
    newCupcake.append(details);
    return newCupcake;
}

function addCupcakeToList(cupcake) {
    const newCupcake = createCupcakeElement(cupcake);
    cupcakeList.append(newCupcake);
}

async function listCupcakes() {
    const cupcakes = await getCupcakes();
    console.log(cupcakes);
    for (cupcake of cupcakes) {
        addCupcakeToList(cupcake);
    }
}

form.addEventListener('submit', async function(e) {
    e.preventDefault();
    const data = {
        flavor: flavor.value,
        size: size.value,
        rating: rating.value,
        image: image.value
    }
    const result = await addNewCupcake(data);
    console.log(result);
    addCupcakeToList(result);
    form.reset();
});

listCupcakes();
