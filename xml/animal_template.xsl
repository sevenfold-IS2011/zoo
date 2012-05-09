<?xml version="1.0"?>
<xsl:stylesheet
	version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:zoo="http://www.zoo.com">
<<<<<<< HEAD
	<xsl:template match="/">
		<h3>Descizione di un animale:</h3>
=======
	<xsl:template match="zoo:zoo">
	<html>
		<body>
		<h3>Descizione degli:</h3>
>>>>>>> 3ee02ccc0794ceb7a00036590d8da28034053958
			<xsl:for-each select="zoo:animal">
				<p>--- Ciao, sono <xsl:value-of select="zoo:name"/>, </p>
				<p>sono un <xsl:value-of select="zoo:gender"/>,</p>
				<p>ho <xsl:value-of select="zoo:age"/> anni, </p>
				<p>vivo nella <xsl:value-of select="zoo:area/zoo:zona"/></p>
				<p>e sono: <xsl:value-of select="zoo:area/zoo:species"/>..</p>

			</xsl:for-each>
	</xsl:template>
</xsl:stylesheet>

