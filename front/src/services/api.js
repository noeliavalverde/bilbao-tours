import config from "@/config.js";

export async function getTours(){
    const settings = {
        method: "GET",
        headers: {
            Authorization: "Bearer",
        },
    };
    const response = await fetch(`${config.API_PATH}/tours`, settings);
    const tours = await response.json();
    return tours;

}

export async function getTourDetail(tourId){
    const settings = {
        method: "GET",
        headers: {
            Authorization: "Bearer",
        },
    };
    const response = await fetch(`${config.API_PATH}/tours/${tourId}`, settings);
    return await response.json();
    

}