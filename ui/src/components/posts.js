
const posts = [
    {
        id:1,
        title: "Reduce your energy consumption",
        content: ["One of the most effective ways to reduce your carbon footprint is to use less energy.",
        "You can do this by turning off, lights and electronics when you're not using them, using energy-efficient appliances, and sealing air leaks in your home."],
        img: "./assets/energy-efficiency.jpg"
    },
    {
        id:2,
        title: "Use sustainable transportation",
        content: ["Instead of driving everywhere, consider walking, biking, or taking public transportation.",
        "This will not only reduce your carbon footprint but also improve your health."],
        img: "./assets/sustainable_transportation.png"
    },
    {
        id:3,
        title: "Reduce your water usage",
        content: ["You can conserve water by taking shorter showers, fixing leaky faucets, and watering your lawn and garden only when necessary"],
        img: "./assets/water_usage.png"
    },
    {
        id:4,
        title: "Eat a plant-based diet",
        content: ["Animal agriculture is a significant contributor to greenhouse gas emissions, so reducing your meat and dairy consumptioncan have a big impact on the environment.",
        "Try incorporating more plant-based meals into your diet."],
        img: "./assets/plant_based_diet.png"
    },
    {
        id:5,
        title: "Support eco-friendly businesses",
        content: ["When shopping, look for products and businesses that prioritize sustainability and eco-friendliness.",
        "This can include buying products made from recycled materials, choosing products with minimal packaging, and supporting local businesses."],
        img: "./assets/eco-shopping.png"
    },
    {
        id:6,
        title: "Get involved in your community",
        content: ["Joining a local environmental organization or volunteering for environmental causes can help you make a positive impact",
        "on the environment and connect with others who share your values."],
        img: "./assets/volunteer.png"
    },
    {
        id:7,
        title: "Reduce your washing",
        content: ["Waste Not Every day by Erin Rhoads , published by Hardie Grant Books and priced at £10, the biggest impact on the environment caused by fashion occurs after we bring clothing home.",
        "In fact, 82% of the energy a garment consumes is a result of the washing and drying we do every week.",
        "Rhoads proposes alternatives to traditional washing, such as spot-cleaning and using diluted vodka or lemon juice to eliminate odors."],
        img: "./assets/washing-machine.png"
    },



]

export function getPosts(){
    return posts;
}
