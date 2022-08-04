
select
    gen_random_uuid() as cht_id,
    longitude
    , latitude
    , housing_median_age
    , total_rooms
    , total_bedrooms
    , population
    , households
    , median_income
    , median_house_value
from {{ source('california_house_training', 'cht_raw' )}}
