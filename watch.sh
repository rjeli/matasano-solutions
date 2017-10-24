inotifywait -m -r -e close_write . | 
  while read _ _ _; do
    echo "==="
    python test.py && echo "OK"
  done