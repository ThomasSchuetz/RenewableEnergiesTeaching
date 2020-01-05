function log_wind_profile(height_measurement, height_calculation, roughness_length, wind_speed_measurement) 
{
    return wind_speed_measurement * Math.log(height_calculation/roughness_length) / Math.log(height_measurement/roughness_length);
}

function transform_profile_to_height(original_wind_profile, height_measurement, height_calculation, roughness_length)
{
    const transformation_factor = log_wind_profile(height_measurement, height_calculation, roughness_length, 1.0);

    var result = [];
    original_wind_profile.forEach(original_wind_speed => {
        result.push(original_wind_speed * transformation_factor);
    });

    return result;
}
