{#  format_json_path from airbyte (this grabs only the first json path)  #}
{% macro airbyte_json_column_grab(model,column_name) -%}
  {%- set variant_keys_query -%}
    SELECT 
        DISTINCT 
        KEY::STRING AS OBJECT_KEYS,
        REGEXP_REPLACE(UPPER(KEY),'( ){1,}','_')::STRING AS COLUMN_NAME_HELPER
    FROM {{model}}
    ,table(flatten({{column_name}}))
  {%- endset -%}
  {%- if execute -%}
    {%- set keys = run_query(variant_keys_query).columns[0].values() -%}
    {%- for key in keys %}
      nullif(to_varchar(json_extract_path_text( {{column_name}}, '"{{key}}"')),'') AS "{{key}}"{% if not loop.last %}, {% endif %}
    {%- endfor -%}
  {%- else %}
    {{ return('NULL')}}
  {%- endif -%}  
{%- endmacro -%} 

{#  format_json_path from airbyte (this grabs only the first json path)  #}
{% macro airbyte_json_column_name_only(model,column_name) -%}
  {%- set variant_keys_query -%}
    SELECT 
        DISTINCT 
        KEY::STRING AS OBJECT_KEYS,
        REGEXP_REPLACE(UPPER(KEY),'( ){1,}','_')::STRING AS COLUMN_NAME_HELPER
    FROM {{model}}
    ,table(flatten({{column_name}}))
  {%- endset -%}
  {%- if execute -%}
    {%- set keys = run_query(variant_keys_query).columns[0].values() -%}
    {%- for key in keys -%}
    "{{key}}"{% if not loop.last %}, {% endif %}
    {%- endfor -%}
  {%- else %}
    {{ return('NULL')}}
  {%- endif -%}  
{%- endmacro -%} 
