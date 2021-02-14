# zad

# Paginacja
## Zmienna do paginacji domyślnie 10
```
query parameter = page=2
export PAGINATION=10
```

## filtrowanie 
```
  query_param=filter
  http://127.0.0.1:8000?filter=example@example.com
```

# Jak odpalić - całość jest umieszczona w dockerze
```
docker-compose up
```

# Restowe api jest pod
```
   http://127.0.0.1:8000/api/search
```

# Todo - nie starczyło czasu na
- [ ] docać do kontenera crontab dodać crona który będzie się odpalać raz dziennie
