Title: BaseRepositoryInterface Base Eloquent Repository
Date: 2013-07-04 10:54
Author: Andrew Elkins
Category: PHP, Programming
Tags: laravel
Slug: baserepositoryinterface
Status: published

Here's a base Eloquent Repository.  
~~~~  
interface BaseRepositoryInterface  
{  
/\*\*  
\* Execute the query and get the first result.  
\*  
\* @param array \$columns  
\* @return :::IlluminateDatabase:::EloquentModel|null|static  
\* @static  
\*/  
public function first(\$columns);

/\*\*  
\* Execute the query and get the first result or throw an exception.  
\*  
\* @param array \$columns  
\* @return :::IlluminateDatabase:::EloquentModel  
\* @static  
\*/  
public function firstOrFail(\$columns);

/\*\*  
\* Execute the query as a "select" statement.  
\*  
\* @param array \$columns  
\* @return
:::IlluminateDatabase:::EloquentCollection|:::Eloquent\[\]|static\[\]  
\* @static  
\*/  
public function get(\$columns);

/\*\*  
\* Pluck a single column from the database.  
\*  
\* @param string \$column  
\* @return mixed|static  
\* @static  
\*/  
public function pluck(\$column);

/\*\*  
\* Get an array with the values of a given column.  
\*  
\* @param string \$column  
\* @param string \$key  
\* @return array  
\* @static  
\*/  
public function lists(\$column, \$key = null);

/\*\*  
\* Get a paginator for the "select" statement.  
\*  
\* @param int \$perPage  
\* @param array \$columns  
\* @return Illuminate:::PaginationPaginator  
\* @static  
\*/  
public function paginate(\$perPage = null, \$columns = array());

/\*\*  
\* Get the hydrated models without eager loading.  
\*  
\* @param array \$columns  
\* @return array  
\* @static  
\*/  
public function getModels(\$columns = array());

/\*\*  
\* Eager load the relationships for the models.  
\*  
\* @param array \$models  
\* @return array  
\* @static  
\*/  
public function eagerLoadRelations(\$models);

/\*\*  
\* Add a relationship count condition to the query.  
\*  
\* @param string \$relation  
\* @param string \$operator  
\* @param int \$count  
\* @param string \$boolean  
\* @return :::IlluminateDatabase:::EloquentBuilder  
\* @static  
\*/  
public function has(\$relation, \$operator = '&gt;=', \$count = 1,
\$boolean = 'and');

/\*\*  
\* Add a relationship count condition to the query with an "or".  
\*  
\* @param string \$relation  
\* @param string \$operator  
\* @param int \$count  
\* @return :::IlluminateDatabase:::EloquentBuilder  
\* @static  
\*/  
public function orHas(\$relation, \$operator = '&gt;=', \$count = 1);

/\*\*  
\* Get the underlying query builder instance.  
\*  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function getQuery();

/\*\*  
\* Set the underlying query builder instance.  
\*  
\* @param :::IlluminateDatabase:::QueryBuilder \$query  
\* @return void  
\* @static  
\*/  
public function setQuery(\$query);

/\*\*  
\* Get the relationships being eagerly loaded.  
\*  
\* @return array  
\* @static  
\*/  
public function getEagerLoads();

/\*\*  
\* Set the relationships being eagerly loaded.  
\*  
\* @param array \$eagerLoad  
\* @return void  
\* @static  
\*/  
public function setEagerLoads(\$eagerLoad);

/\*\*  
\* Get the model instance being queried.  
\*  
\* @return :::IlluminateDatabase:::EloquentModel  
\* @static  
\*/  
public function getModel();

/\*\*  
\* Set a model instance for the model being queried.  
\*  
\* @param :::IlluminateDatabase:::EloquentModel \$model  
\* @return :::IlluminateDatabase:::EloquentBuilder  
\* @static  
\*/  
public function setModel(\$model);

/\*\*  
\* Set the columns to be selected.  
\*  
\* @param array \$columns  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function select(\$columns = array());

/\*\*  
\* Add a new select column to the query.  
\*  
\* @param mixed \$column  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function addSelect(\$column);

/\*\*  
\* Force the query to only return distinct results.  
\*  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function distinct();

/\*\*  
\* Set the table which the query is targeting.  
\*  
\* @param string \$table  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function from(\$table);

/\*\*  
\* Add a join clause to the query.  
\*  
\* @param string \$table  
\* @param string \$first  
\* @param string \$operator  
\* @param string \$second  
\* @param string \$type  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function join(\$table, \$first, \$operator = null, \$second =
null, \$type = 'inner');

/\*\*  
\* Add a left join to the query.  
\*  
\* @param string \$table  
\* @param string \$first  
\* @param string \$operator  
\* @param string \$second  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function leftJoin(\$table, \$first, \$operator = null, \$second =
null);

/\*\*  
\* Add a basic where clause to the query.  
\*  
\* @param string \$column  
\* @param string \$operator  
\* @param mixed \$value  
\* @param string \$boolean  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function where(\$column, \$operator = null, \$value = null,
\$boolean = 'and');

/\*\*  
\* Add an "or where" clause to the query.  
\*  
\* @param string \$column  
\* @param string \$operator  
\* @param mixed \$value  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function orWhere(\$column, \$operator = null, \$value = null);

/\*\*  
\* Add a raw where clause to the query.  
\*  
\* @param string \$sql  
\* @param array \$bindings  
\* @param string \$boolean  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function whereRaw(\$sql, \$bindings = array(), \$boolean =
'and');

/\*\*  
\* Add a raw or where clause to the query.  
\*  
\* @param string \$sql  
\* @param array \$bindings  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function orWhereRaw(\$sql, \$bindings = array());

/\*\*  
\* Add a where between statement to the query.  
\*  
\* @param string \$column  
\* @param array \$values  
\* @param string \$boolean  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function whereBetween(\$column, \$values, \$boolean = 'and');

/\*\*  
\* Add an or where between statement to the query.  
\*  
\* @param string \$column  
\* @param array \$values  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function orWhereBetween(\$column, \$values);

/\*\*  
\* Add a nested where statement to the query.  
\*  
\* @param Closure \$callback  
\* @param string \$boolean  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function whereNested(\$callback, \$boolean = 'and');

/\*\*  
\* Add an exists clause to the query.  
\*  
\* @param Closure \$callback  
\* @param string \$boolean  
\* @param bool \$not  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function whereExists(\$callback, \$boolean = 'and', \$not =
false);

/\*\*  
\* Add an or exists clause to the query.  
\*  
\* @param Closure \$callback  
\* @param bool \$not  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function orWhereExists(\$callback, \$not = false);

/\*\*  
\* Add a where not exists clause to the query.  
\*  
\* @param Closure \$calback  
\* @param string \$boolean  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function whereNotExists(\$callback, \$boolean = 'and');

/\*\*  
\* Add a where not exists clause to the query.  
\*  
\* @param Closure \$calback  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function orWhereNotExists(\$callback);

/\*\*  
\* Add a "where in" clause to the query.  
\*  
\* @param string \$column  
\* @param mixed \$values  
\* @param string \$boolean  
\* @param bool \$not  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function whereIn(\$column, \$values, \$boolean = 'and', \$not =
false);

/\*\*  
\* Add an "or where in" clause to the query.  
\*  
\* @param string \$column  
\* @param mixed \$values  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function orWhereIn(\$column, \$values);

/\*\*  
\* Add a "where not in" clause to the query.  
\*  
\* @param string \$column  
\* @param mixed \$values  
\* @param string \$boolean  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function whereNotIn(\$column, \$values, \$boolean = 'and');

/\*\*  
\* Add an "or where not in" clause to the query.  
\*  
\* @param string \$column  
\* @param mixed \$values  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function orWhereNotIn(\$column, \$values);

/\*\*  
\* Add a "where null" clause to the query.  
\*  
\* @param string \$column  
\* @param string \$boolean  
\* @param bool \$not  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function whereNull(\$column, \$boolean = 'and', \$not = false);

/\*\*  
\* Add an "or where null" clause to the query.  
\*  
\* @param string \$column  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function orWhereNull(\$column);

/\*\*  
\* Add a "where not null" clause to the query.  
\*  
\* @param string \$column  
\* @param string \$boolean  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function whereNotNull(\$column, \$boolean = 'and');

/\*\*  
\* Add an "or where not null" clause to the query.  
\*  
\* @param string \$column  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function orWhereNotNull(\$column);

/\*\*  
\* Handles dynamic "where" clauses to the query.  
\*  
\* @param string \$method  
\* @param string \$parameters  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function dynamicWhere(\$method, \$parameters);

/\*\*  
\* Add a "group by" clause to the query.  
\*  
\* @param dynamic \$columns  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function groupBy();

/\*\*  
\* Add a "having" clause to the query.  
\*  
\* @param string \$column  
\* @param string \$operator  
\* @param string \$value  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function having(\$column, \$operator = null, \$value = null);

/\*\*  
\* Add a raw having clause to the query.  
\*  
\* @param string \$sql  
\* @param array \$bindings  
\* @param string \$boolean  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function havingRaw(\$sql, \$bindings = array(), \$boolean =
'and');

/\*\*  
\* Add a raw or having clause to the query.  
\*  
\* @param string \$sql  
\* @param array \$bindings  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function orHavingRaw(\$sql, \$bindings = array());

/\*\*  
\* Add an "order by" clause to the query.  
\*  
\* @param string \$column  
\* @param string \$direction  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function orderBy(\$column, \$direction = 'asc');

/\*\*  
\* Set the "offset" value of the query.  
\*  
\* @param int \$value  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function skip(\$value);

/\*\*  
\* Set the "limit" value of the query.  
\*  
\* @param int \$value  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function take(\$value);

/\*\*  
\* Set the limit and offset for a given page.  
\*  
\* @param int \$page  
\* @param int \$perPage  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function forPage(\$page, \$perPage = 15);

/\*\*  
\* Add a union statement to the query.  
\*  
\* @param :::IlluminateDatabase:::QueryBuilder|:::Closure \$query  
\* @param bool \$all  
\* @return Illuminate:::DatabaseQuery:::Builder|static  
\* @static  
\*/  
public function union(\$query, \$all = false);

/\*\*  
\* Add a union all statement to the query.  
\*  
\* @param Illuminate:::DatabaseQuery:::Builder|Closure \$query  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function unionAll(\$query);

/\*\*  
\* Get the SQL representation of the query.  
\*  
\* @return string  
\* @static  
\*/  
public function toSql();

/\*\*  
\* Indicate that the query results should be cached.  
\*  
\* @param int \$minutes  
\* @param string \$key  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function remember(\$minutes, \$key = null);

/\*\*  
\* Execute the query as a fresh "select" statement.  
\*  
\* @param array \$columns  
\* @return array  
\* @static  
\*/  
public function getFresh(\$columns = array());

/\*\*  
\* Execute the query as a cached "select" statement.  
\*  
\* @param array \$columns  
\* @return array  
\* @static  
\*/  
public function getCached(\$columns = array());

/\*\*  
\* Get a unique cache key for the complete query.  
\*  
\* @return string  
\* @static  
\*/  
public function getCacheKey();

/\*\*  
\* Generate the unique cache key for the query.  
\*  
\* @return string  
\* @static  
\*/  
public function generateCacheKey();

/\*\*  
\* Concatenate values of a given column as a string.  
\*  
\* @param string \$column  
\* @param string \$glue  
\* @return string  
\* @static  
\*/  
public function implode(\$column, \$glue = null);

/\*\*  
\* Build a paginator instance from a raw result array.  
\*  
\* @param :::IlluminatePagination:::Environment \$paginator  
\* @param array \$results  
\* @param int \$perPage  
\* @return Illuminate:::PaginationPaginator  
\* @static  
\*/  
public function buildRawPaginator(\$paginator, \$results, \$perPage);

/\*\*  
\* Get the count of the total records for pagination.  
\*  
\* @return int  
\* @static  
\*/  
public function getPaginationCount();

/\*\*  
\* Determine if any rows exist for the current query.  
\*  
\* @return bool  
\* @static  
\*/  
public function exists();

/\*\*  
\* Retrieve the "count" result of the query.  
\*  
\* @param string \$column  
\* @return int  
\* @static  
\*/  
public function count(\$column = '\*');

/\*\*  
\* Retrieve the minimum value of a given column.  
\*  
\* @param string \$column  
\* @return mixed  
\* @static  
\*/  
public function min(\$column);

/\*\*  
\* Retrieve the maximum value of a given column.  
\*  
\* @param string \$column  
\* @return mixed  
\* @static  
\*/  
public function max(\$column);

/\*\*  
\* Retrieve the sum of the values of a given column.  
\*  
\* @param string \$column  
\* @return mixed  
\* @static  
\*/  
public function sum(\$column);

/\*\*  
\* Retrieve the average of the values of a given column.  
\*  
\* @param string \$column  
\* @return mixed  
\* @static  
\*/  
public function avg(\$column);

/\*\*  
\* Execute an aggregate function on the database.  
\*  
\* @param string \$function  
\* @param array \$columns  
\* @return mixed  
\* @static  
\*/  
public function aggregate(\$function, \$columns = array());

/\*\*  
\* Insert a new record into the database.  
\*  
\* @param array \$values  
\* @return bool  
\* @static  
\*/  
public function insert(\$values);

/\*\*  
\* Insert a new record and get the value of the primary key.  
\*  
\* @param array \$values  
\* @param string \$sequence  
\* @return int  
\* @static  
\*/  
public function insertGetId(\$values, \$sequence = null);

/\*\*  
\* Run a truncate statement on the table.  
\*  
\* @return void  
\* @static  
\*/  
public function truncate();

/\*\*  
\* Merge an array of where clauses and bindings.  
\*  
\* @param array \$wheres  
\* @param array \$bindings  
\* @return void  
\* @static  
\*/  
public function mergeWheres(\$wheres, \$bindings);

/\*\*  
\* Get a copy of the where clauses and bindings in an array.  
\*  
\* @return array  
\* @static  
\*/  
public function getAndResetWheres();

/\*\*  
\* Create a raw database expression.  
\*  
\* @param mixed \$value  
\* @return :::IlluminateDatabase:::QueryExpression  
\* @static  
\*/  
public function raw(\$value);

/\*\*  
\* Get the current query value bindings.  
\*  
\* @return array  
\* @static  
\*/  
public function getBindings();

/\*\*  
\* Set the bindings on the query builder.  
\*  
\* @param array \$bindings  
\* @return void  
\* @static  
\*/  
public function setBindings(\$bindings);

/\*\*  
\* Merge an array of bindings into our bindings.  
\*  
\* @param :::IlluminateDatabase:::QueryBuilder \$query  
\* @return :::IlluminateDatabase:::QueryBuilder|static  
\* @static  
\*/  
public function mergeBindings(\$query);

/\*\*  
\* Get the database query processor instance.  
\*  
\* @return :::IlluminateDatabase:::QueryProcessors:::Processor  
\* @static  
\*/  
public function getProcessor();

/\*\*  
\* Get the query grammar instance.  
\*  
\* @return Illuminate:::DatabaseGrammar  
\* @static  
\*/  
public function getGrammar();  
}  
~~~~
