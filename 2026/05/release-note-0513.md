
# Title: May 12, 2026 
Link: https://docs.cloud.google.com/release-notes#May_12_2026<br>
## Compute Engine
### Fixed

**原文:**
A vulnerability in AMD firmware (CVE-2025-61971, CVE-2025-61972, CVE-2024-36315) that could compromise SEV-SNP guests has been addressed.
For more information, see the GCP-2026-031 security bulletin.

**説明:**
AMD社製プロセッサのファームウェアに存在する複数の脆弱性（CVE-2025-61971, CVE-2025-61972, CVE-2024-36315）が修正されました。これらの脆弱性は、Google CloudのConfidential VMなどで利用されるSEV-SNP（Secure Encrypted Virtualization-Secure Nested Paging）機能を使用するゲストVMのセキュリティを危険にさらす可能性がありました。Google Cloudはこの脆弱性に対処し、基盤となるインフラストラクチャを更新しました。詳細については、GCP-2026-031セキュリティ速報をご参照ください。

**影響有無:**
影響なし（ユーザー側での直接的な操作は不要）。
この修正はGoogle Cloud側で基盤のファームウェアに対して適用されており、ユーザーが明示的にVMやサービスに何らかの変更を加える必要はありません。SEV-SNPを使用しているVMにおいては、既存のセキュリティリスクが解消され、より安全に利用できるようになるため、セキュリティ面でプラスの影響があります。サービス運用への機能的な変更や互換性の問題は発生しません。

**対処方法:**
ユーザー側での特別な対処は不要です。Google Cloudがプラットフォームレベルで対応済みのため、引き続きサービスをご利用いただけます。

**用語説明:**
*   **SEV-SNP (Secure Encrypted Virtualization-Secure Nested Paging):** AMD EPYC™プロセッサに搭載されているセキュリティ機能で、Confidential VMの基盤技術の一つです。仮想マシン（VM）のメモリとCPUレジスタを暗号化し、ホストOSやハイパーバイザーからの不正アクセスから保護することで、ゲストVMの機密性を高めます。
*   **ファームウェア:** ハードウェアを制御するための低レベルなソフトウェアです。

---

## Compute Engine
### Fixed

**原文:**
A vulnerability (CVE-2025-54518) about potential corruption within the micro-operation (OP) cache in Zen 2 microarchitecture processors was discovered and has been addressed.
For more information, see the GCP-2026-032 security bulletin.

**説明:**
AMD社製Zen 2マイクロアーキテクチャプロセッサ（Google CloudのN2Dマシンタイプなどで利用されるAMD EPYC™ Rome CPUに搭載）のマイクロオペレーション（OP）キャッシュ内に、潜在的なデータ破損を引き起こす脆弱性（CVE-2025-54518）が発見され、修正されました。Google Cloudはこの脆弱性に対処し、基盤となるインフラストラクチャを更新しました。詳細については、GCP-2026-032セキュリティ速報をご参照ください。

**影響有無:**
影響なし（ユーザー側での直接的な操作は不要）。
この修正もGoogle Cloud側で基盤のプロセッサや関連ファームウェアに対して適用されており、ユーザーが明示的にVMやサービスに何らかの変更を加える必要はありません。Zen 2ベースのVMを利用している場合、この脆弱性による潜在的なリスクが解消され、安定性が向上します。サービス運用への機能的な変更や互換性の問題は発生しません。

**対処方法:**
ユーザー側での特別な対処は不要です。Google Cloudがプラットフォームレベルで対応済みのため、引き続きサービスをご利用いただけます。

**用語説明:**
*   **Zen 2マイクロアーキテクチャ:** AMDが開発したCPUのアーキテクチャで、高いパフォーマンスと効率性を特徴とします。Google Cloudでは、N2DマシンタイプなどのVMインスタンスで利用されるAMD EPYC Romeプロセッサにこのアーキテクチャが採用されています。
*   **マイクロオペレーション（OP）キャッシュ:** CPU内部の重要なコンポーネントの一つです。CPUは複雑な命令を直接実行するのではなく、より単純な「マイクロオペレーション」に分解して処理します。マイクロオペレーションキャッシュは、これらのマイクロオペレーションを一時的に保存することで、繰り返し実行される処理の効率を高め、CPUのパフォーマンスを向上させます。
# Title: May 11, 2026 
Link: https://docs.cloud.google.com/release-notes#May_11_2026<br>
# AlloyDB for PostgreSQL
## Announcement
原文: AlloyDB now offers extended support for clusters running major PostgreSQL versions that have reached their end-of-life (EOL) as defined by the PostgreSQL community. Extended support provides an additional three years of support after the end of regular support, giving you more time to plan and perform major version upgrades. For more information, see Extended support for AlloyDB for PostgreSQL.

[Extended support for AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/extended-support)

説明：
AlloyDB for PostgreSQLにおいて、PostgreSQLコミュニティによってEOL（End-of-Life）とされたメジャーバージョンのクラスタに対して、延長サポートが提供されるようになりました。この延長サポートは、通常のサポート期間終了後、さらに3年間サポートを延長するもので、メジャーバージョンアップグレードの計画と実行により多くの時間的余裕を持つことができるようになります。

影響有無：
**影響：なし（またはプラスの影響）**
これは既存のサービスに対して強制的な変更を伴うものではなく、新しいサポートオプションが追加されたものです。AlloyDB for PostgreSQLを利用しており、PostgreSQLの古いメジャーバージョンを使用しているユーザーにとっては、EOL後のアップグレード猶予期間が増えるため、運用計画の柔軟性が向上するというプラスの影響があります。

対処方法：
**対応不要**
このアナウンスは、既存のAlloyDBクラスタの運用に直接的な変更を求めるものではありません。ただし、現在AlloyDB for PostgreSQLを運用しており、EOL間近またはすでにEOLを迎えたPostgreSQLメジャーバージョンを利用している場合は、この延長サポートを活用して、計画的なメジャーバージョンアップグレードを行うことを検討できます。これにより、システムの安定稼働を維持しつつ、十分なテスト期間を確保することが可能になります。

用語説明：
*   **AlloyDB for PostgreSQL:** Google Cloudが提供する、PostgreSQL互換のフルマネージドデータベースサービスです。高性能、高可用性、スケーラビリティを特徴としています。
*   **EOL (End-of-Life):** ソフトウェアや製品のサポートが公式に終了する時点を指します。EOL後は通常、セキュリティパッチの提供や技術サポートが終了します。
*   **PostgreSQLコミュニティ:** オープンソースのリレーショナルデータベースシステムであるPostgreSQLの開発、保守、サポートを行っているコミュニティです。各バージョンのサポートライフサイクルを定めています。
*   **延長サポート (Extended Support):** 通常のサポート期間が終了した後も、一定期間（このケースでは追加の3年間）提供される有償または特定の条件下のサポートサービスです。これにより、セキュリティアップデートや重要なバグ修正が継続して提供される場合があります。
*   **メジャーバージョンアップグレード:** データベースシステムのメジャーバージョン（例：PostgreSQL 14から15）を更新することです。通常、大幅な機能追加や改善が含まれますが、互換性のない変更（Breaking Change）が含まれる場合もあるため、慎重な計画とテストが必要です。