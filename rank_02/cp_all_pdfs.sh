mkdir -p pdfs
for d in */; do
  [ -f "$d/en.subject.pdf" ] && cp "$d/en.subject.pdf" "pdfs/${d%/}.pdf"
done
