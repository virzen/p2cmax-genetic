for i in {1..20}; do
  ./pcmax_generate.py $i > instance.tmp
  GREEDY=$(./pcmax_greedy.py instance.tmp)
  GENETIC=$(./pcmax_genetic.py instance.tmp)
  echo $GREEDY $GENETIC >> results40-4.txt
done;
