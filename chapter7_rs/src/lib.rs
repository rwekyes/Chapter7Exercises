//! Think Python, chapter 7 exercises 7.9.7 and 7.9.8, written in Rust and
//! exposed to Python with PyO3. All comparisons ignore case.

use pyo3::prelude::*;

#[pymodule]
mod chapter7_rs {
    use pyo3::prelude::*;

    /// Checks whether a word uses any of the given letters.
    #[pyfunction]
    pub fn uses_any(word: &str, letters: &str) -> bool {
        let letters = letters.to_lowercase();
        for letter in word.to_lowercase().chars() {
            if letters.contains(letter) {
                return true;
            }
        }
        false
    }

    /// Checks whether a word uses only the available letters.
    #[pyfunction]
    pub fn uses_only(word: &str, available: &str) -> bool {
        let available = available.to_lowercase();
        for letter in word.to_lowercase().chars() {
            if !available.contains(letter) {
                return false;
            }
        }
        true
    }

    /// 7.9.7: Checks whether a word uses all required letters, using uses_only.
    ///
    /// If the word uses every required letter, then the required letters
    /// use only letters found in the word -- so just flip the arguments.
    #[pyfunction]
    pub fn uses_all_via_only(word: &str, required: &str) -> bool {
        uses_only(required, word)
    }

    /// 7.9.8: Checks whether a word uses all required letters, using uses_any.
    ///
    /// Asks uses_any about one required letter at a time; if any single
    /// letter is missing from the word, the word fails.
    #[pyfunction]
    pub fn uses_all_via_any(word: &str, required: &str) -> bool {
        let mut buf = [0; 4];
        for letter in required.chars() {
            if !uses_any(word, letter.encode_utf8(&mut buf)) {
                return false;
            }
        }
        true
    }
}

#[cfg(test)]
mod tests {
    use super::chapter7_rs::*;

    #[test]
    fn uses_any_works() {
        assert!(uses_any("banana", "n"));
        assert!(!uses_any("apple", "xyz"));
    }

    #[test]
    fn uses_only_works() {
        assert!(uses_only("banana", "ban"));
        assert!(!uses_only("apple", "apl"));
        assert!(uses_only("color", "ACDLORT"));
    }

    #[test]
    fn uses_all_versions_agree() {
        let cases = [
            ("banana", "ban", true),
            ("apple", "api", false),
            ("funky", "ykfnu", true),
            ("geddylee", "rush", false),
            ("CARTLOAD", "acdlort", true),
            ("anything", "", true),
        ];
        for (word, required, expected) in cases {
            assert_eq!(uses_all_via_only(word, required), expected, "{word} {required}");
            assert_eq!(uses_all_via_any(word, required), expected, "{word} {required}");
        }
    }
}
