# Output

Generated PDFs, build logs, and review artifacts belong here. The editable
source remains in `../paper/`.

The default build target is `NSE_draft.pdf`.

If `NSE_draft.pdf` is open in a PDF viewer and Windows locks it, the build
script writes the newly compiled file to `NSE_draft_pending.pdf` instead of
failing. Close the viewer and run the build again to replace the default file.
