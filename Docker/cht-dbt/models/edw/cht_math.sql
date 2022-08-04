select
    *,
    case when housing_median_age < 18 then 'de_0_ate_18'
         when housing_median_age >= 18 and housing_median_age < 29 then 'ate_29'
         when housing_median_age >=29 and housing_median_age <37 then 'ate_37'
         else 'acima_37'
    end as hma_cat,
    case when longitude < -119 then 'norte'
         else 'sul'
    end as c_ns
from {{ ref('stg_cht_raw') }}