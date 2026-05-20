import click
import os
from pathlib import Path
from .config import Config
from .vector_index import MultiLanguageIndexer, VectorIndexer
from .align_viz import Aligner
from .report_viz import Reporter
from .utils import logger

@click.command()
@click.option('--input', required=True, help='Path to Portuguese article (.txt)')
@click.option('--out_dir', default='output_viz', help='Output directory')
@click.option('--include_corpora', multiple=True, help='Include specific corpora (e.g. French)')
@click.option('--volume', default=None, help='Direct alignment against this volume (bypass search)')
@click.option('--index_dir', default=None, help='Custom index directory path')
@click.option('--title_left', default=None, help='Override left column title')
@click.option('--title_right', default=None, help='Override right column title')
def main(input, out_dir, include_corpora, volume, index_dir, title_left, title_right):
    config = Config()
    
    if index_dir:
        logger.info(f"Using custom index at: {index_dir}")
        indexer = VectorIndexer(config, index_path=index_dir)
        indexer.load()
    else:
        indexer = MultiLanguageIndexer(config, base_dir='index_data')
        
    aligner = Aligner(config)
    reporter = Reporter(out_dir)
    
    pt_path = Path(input)
    with open(pt_path, 'r', encoding='utf-8') as f:
        text_pt = f.read()
    
    logger.info(f"Processing {pt_path.name}...")
    
    if volume:
        logger.info(f"Direct alignment mode: {volume}")
        all_volume_alignments = aligner.align_single_volume(text_pt, volume, indexer)
        secondary_matches = []
    else:
        all_volume_alignments, secondary_matches = aligner.process_document(
            text_pt, indexer, include_corpora=list(include_corpora)
        )
    
    if not all_volume_alignments:
        logger.error("No matches found to visualize.")
        return
        
    reporter.save_results(
        pt_path.name,
        text_pt,
        text_pt,
        all_volume_alignments,
        secondary_matches,
        used_corpora=list(include_corpora) if include_corpora else [volume] if volume else ["All"],
        title_left=title_left,
        title_right=title_right
    )
    
    logger.info(f"Visualization complete. Files saved to {out_dir}")

if __name__ == "__main__":
    main()
